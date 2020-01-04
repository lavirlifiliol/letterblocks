package lakmatiol.letterblocks;

import org.sandboxpowered.sandbox.api.SandboxAPI;
import org.sandboxpowered.sandbox.api.addon.Addon;
import org.sandboxpowered.sandbox.api.block.BaseBlock;
import org.sandboxpowered.sandbox.api.block.Block;
import org.sandboxpowered.sandbox.api.block.Material;
import org.sandboxpowered.sandbox.api.item.BaseBlockItem;
import org.sandboxpowered.sandbox.api.item.Item;
import org.sandboxpowered.sandbox.api.util.Identity;

import java.util.HashMap;
import java.util.function.Supplier;

public class LetterBlocks implements Addon {
    public static final String MODID = "letterblocks";

    private void registerBlock(SandboxAPI api, Identity id, BaseBlock block) {
        api.register(id, block);
        api.register(id, new BaseBlockItem(block, new Item.Settings()));
    }

    @Override
    public void init(SandboxAPI api) {
        Block.Settings common = new Block.Settings(Material.WOOD);
        for(char name = 'a'; name <= 'z'; name++) {
            registerBlock(api, Identity.of(MODID, String.format("%c_upper", name)), new BaseBlock(common));
            registerBlock(api, Identity.of(MODID, String.format("%c_lower", name)), new BaseBlock(common));

        }
    }
}
