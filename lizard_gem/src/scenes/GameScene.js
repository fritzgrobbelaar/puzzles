export default class GameScene extends Phaser.Scene {
    constructor() {
        super({ key: 'GameScene' });
        this.player = null;
        this.gems = {
            ruby: { collected: 0, total: 2 },
            sapphire: { collected: 0, total: 2 }
        };
        this.enemies = [];
        this.projectiles = null;
        this.portal = null;
        this.gemText = null;
        this.lastFired = 0;
    }

    preload() {
        // Temporary colored rectangles for placeholders
        this.load.image('player', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGklEQVRYR+3BAQEAAACCIP+vbkhAAQAAAO8GECAAAZf3V9cAAAAASUVORK5CYII=');
        this.load.image('enemy', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGklEQVRYR+3BAQEAAACCIP+vbkhAAQAAAO8GECAAAZf3V9cAAAAASUVORK5CYII=');
        this.load.image('projectile', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGklEQVR42mNkYGD4z0AEYBxVOBKUjh07RhAHANRfDcEzef8KAAAAAElFTkSuQmCC');
        this.load.image('ruby', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGklEQVRYR+3BAQEAAACCIP+vbkhAAQAAAO8GECAAAZf3V9cAAAAASUVORK5CYII=');
        this.load.image('sapphire', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGklEQVRYR+3BAQEAAACCIP+vbkhAAQAAAO8GECAAAZf3V9cAAAAASUVORK5CYII=');
        this.load.image('portal', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGklEQVRYR+3BAQEAAACCIP+vbkhAAQAAAO8GECAAAZf3V9cAAAAASUVORK5CYII=');
    }

    create() {
        // Create player
        this.player = this.physics.add.sprite(400, 300, 'player');
        this.player.setCollideWorldBounds(true);
        this.player.setTint(0x00ff00); // Green for poison lizard

        // Create projectile group
        this.projectiles = this.physics.add.group();

        // Create enemies
        for (let i = 0; i < 4; i++) {
            const enemy = this.physics.add.sprite(
                Phaser.Math.Between(100, 700),
                Phaser.Math.Between(100, 500),
                'enemy'
            );
            enemy.setTint(0x808080); // Gray for rock crawlers
            this.enemies.push(enemy);
        }

        // Create gems
        this.createGem('ruby', 0xff0000);
        this.createGem('ruby', 0xff0000);
        this.createGem('sapphire', 0x0000ff);
        this.createGem('sapphire', 0x0000ff);

        // Create portal (initially invisible)
        this.portal = this.physics.add.sprite(700, 100, 'portal');
        this.portal.setTint(0xffffff);
        this.portal.setVisible(false);
        this.portal.setActive(false);

        // Setup collisions
        this.physics.add.overlap(this.projectiles, this.enemies, this.handleProjectileHit, null, this);
        this.physics.add.overlap(this.player, this.portal, this.handlePortalCollision, null, this);

        // Create UI
        this.gemText = this.add.text(16, 16, '', { fontSize: '18px', fill: '#fff' });
        this.updateGemText();

        // Setup input
        this.cursors = this.input.keyboard.createCursorKeys();
    }

    createGem(type, tint) {
        const gem = this.physics.add.sprite(
            Phaser.Math.Between(100, 700),
            Phaser.Math.Between(100, 500),
            type
        );
        gem.setTint(tint);
        gem.type = type;
        this.physics.add.overlap(this.player, gem, () => this.collectGem(gem), null, this);
    }

    update() {
        // Player movement
        const speed = 200;
        this.player.setVelocity(0);

        if (this.cursors.left.isDown) {
            this.player.setVelocityX(-speed);
        } else if (this.cursors.right.isDown) {
            this.player.setVelocityX(speed);
        }

        if (this.cursors.up.isDown) {
            this.player.setVelocityY(-speed);
        } else if (this.cursors.down.isDown) {
            this.player.setVelocityY(speed);
        }

        // Shooting
        if (this.cursors.space.isDown && this.time.now > this.lastFired + 500) {
            this.shoot();
            this.lastFired = this.time.now;
        }

        // Enemy movement (simple following behavior)
        this.enemies.forEach(enemy => {
            if (enemy.active) {
                const angle = Phaser.Math.Angle.Between(
                    enemy.x, enemy.y,
                    this.player.x, this.player.y
                );
                const speed = 100;
                enemy.setVelocityX(Math.cos(angle) * speed);
                enemy.setVelocityY(Math.sin(angle) * speed);
            }
        });
    }

    shoot() {
        const projectile = this.projectiles.create(this.player.x, this.player.y, 'projectile');
        projectile.setTint(0x00ff00); // Green poison
        
        const pointer = this.input.activePointer;
        const angle = Phaser.Math.Angle.Between(
            this.player.x, this.player.y,
            this.input.x, this.input.y
        );

        const speed = 400;
        projectile.setVelocity(
            Math.cos(angle) * speed,
            Math.sin(angle) * speed
        );

        // Destroy projectile after 1 second
        this.time.delayedCall(1000, () => {
            projectile.destroy();
        });
    }

    handleProjectileHit(projectile, enemy) {
        projectile.destroy();
        enemy.destroy();
        
        // Remove from enemies array
        const index = this.enemies.indexOf(enemy);
        if (index > -1) {
            this.enemies.splice(index, 1);
        }

        // If last enemy in a group, drop a gem
        if (this.enemies.length === 0) {
            // Find a gem type that isn't fully collected
            const gemTypes = Object.keys(this.gems).filter(
                type => this.gems[type].collected < this.gems[type].total
            );
            
            if (gemTypes.length > 0) {
                const type = gemTypes[0];
                const tint = type === 'ruby' ? 0xff0000 : 0x0000ff;
                this.createGem(type, tint);
            }
        }
    }

    collectGem(gem) {
        gem.destroy();
        this.gems[gem.type].collected++;
        this.updateGemText();

        // Check if all gems are collected
        const allCollected = Object.values(this.gems).every(
            g => g.collected === g.total
        );

        if (allCollected) {
            this.portal.setVisible(true);
            this.portal.setActive(true);
        }
    }

    handlePortalCollision() {
        if (this.portal.active) {
            // For MVP, just restart the level
            this.scene.restart();
        }
    }

    updateGemText() {
        this.gemText.setText(
            `Rubies: ${this.gems.ruby.collected}/${this.gems.ruby.total}\n` +
            `Sapphires: ${this.gems.sapphire.collected}/${this.gems.sapphire.total}`
        );
    }
} 