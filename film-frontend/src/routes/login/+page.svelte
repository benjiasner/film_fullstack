<script>
    let username = ''
    let password = ''
    let errors = {}
</script>

<div class="col-12 col-md-4">
    <h2 class="my-4">Log in</h2>

    <form>
        <div class="mb-3">
            <input class="form-control" type="text" placeholder="username" bind:value={username} />
        </div>
        <div class="mb-3">
            <input class="form-control" type="text" placeholder="password" bind:value={password} />
        </div>
        <button class="btn btn-primary" type="submit">Log in</button>
    </form>
</div>