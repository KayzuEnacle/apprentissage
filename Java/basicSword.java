public class Epee {
    private int degats;
    private boolean effetFeu;
    private boolean sharpness;

    public Epee() {
        this.degats = 67;
        this.effetFeu = true;
        this.sharpness = true;
    }

    public int getDegats() {
        return this.degats;
    }

    public boolean hasEffetFeu() {
        return this.effetFeu;
    }

    public boolean hasSharpness() {
        return this.sharpness;
    }
}

