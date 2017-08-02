BEGIN;
--
-- Create model Game
--
CREATE TABLE `dashboard_game` (
  `id`         INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `created_at` DATETIME(6)            NOT NULL
);
--
-- Create model Player
--
CREATE TABLE `dashboard_player` (
  `id`         INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name`       VARCHAR(250)           NOT NULL UNIQUE,
  `created_at` DATETIME(6)            NOT NULL
);
--
-- Create model Score
--
CREATE TABLE `dashboard_score` (
  `id`        INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `score`     INTEGER                NOT NULL,
  `Player_id` INTEGER                NOT NULL
);
--
-- Add field Score1 to game
--
ALTER TABLE `dashboard_game`
  ADD COLUMN `Score1_id` INTEGER NOT NULL;
--
-- Add field Score2 to game
--
ALTER TABLE `dashboard_game`
  ADD COLUMN `Score2_id` INTEGER NOT NULL;
--
-- Add field Winner to game
--
ALTER TABLE `dashboard_game`
  ADD COLUMN `Winner_id` INTEGER NOT NULL;
ALTER TABLE `dashboard_score`
  ADD CONSTRAINT `dashboard_score_Player_id_8abdd4ff_fk_dashboard_player_id` FOREIGN KEY (`Player_id`) REFERENCES `dashboard_player` (`id`);
ALTER TABLE `dashboard_game`
  ADD CONSTRAINT `dashboard_game_Score1_id_395a946d_fk_dashboard_score_id` FOREIGN KEY (`Score1_id`) REFERENCES `dashboard_score` (`id`);
ALTER TABLE `dashboard_game`
  ADD CONSTRAINT `dashboard_game_Score2_id_13ccec6d_fk_dashboard_score_id` FOREIGN KEY (`Score2_id`) REFERENCES `dashboard_score` (`id`);
ALTER TABLE `dashboard_game`
  ADD CONSTRAINT `dashboard_game_Winner_id_909ed200_fk_dashboard_player_id` FOREIGN KEY (`Winner_id`) REFERENCES `dashboard_player` (`id`);
COMMIT;