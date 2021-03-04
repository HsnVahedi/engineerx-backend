describe("My First Test", () => {
  it('clicking "type" shows the right headings', () => {
    cy.visit("/");

    cy.url().should("include", "/posts");
  });
});
